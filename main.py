import openai
import os
from pathlib import Path
import argparse
from tqdm import tqdm

from llm_security import llm_config
from llm_security import game_config
from llm_security import util
from llm_security import communicate
from llm_security import eval_plot

RESULT_DIR = Path("./result").absolute()

def main():
    openai.api_key = os.getenv('OPENAI_API_KEY')

    parser = argparse.ArgumentParser(description='llm-security argument parsin')
    parser.add_argument("--debug", default=False, type=bool)
    parser.add_argument("--use_prev", default=False, type=bool)
    parser.add_argument('-m','--models', action='append', help='One or more models to run (gpt4, gpt3.5, gpt3)', required=True, type=str)
    parser.add_argument("--version", default="", type=str)
    parser.add_argument("--num_trial", default=20, type=int)
    parser.add_argument("--game", default="bandit", type=str)

    args = parser.parse_args()
    abbrs = sorted(args.models)
    num_trial = args.num_trial if not args.debug else 1
    if args.debug:
      print("Debug mode")

    print(f"Models to run: {abbrs}")

    if args.use_prev:
        print("Use previous experimentation result")
        version = args.version
        if version == "":
            raise ValueError("version should be specified when using previous version")
    else:
        print("Start new experimentation")
        version = util.get_new_version()
    version_dir = RESULT_DIR / version
    print(f"Version directory: {version_dir}")

    if args.debug:
      for abbr in abbrs:
        print("#"*10 + f" {abbr} " + "#"*10)
        model = llm_config.MODEL_NAME_BY_ABBR[abbr]
        messages = communicate.get_initial_messages(model, llm_config.PRELUDE)
        print(communicate.get_model_response(model, messages, llm_config.PRELUDE))        

    if args.debug:
      for abbr in abbrs:
        print("#"*10 + f" {abbr} " + "#"*10)
        model = llm_config.MODEL_NAME_BY_ABBR[abbr]  
        resp_df, answer = communicate.attempt_level(args.game, 0, 50, model=model, verbose=True, sleep_time=.5, max_ssh_len=1000)
        is_correct = communicate.is_answer_correct(args.game, 0, answer)
        print(f"Take {len(resp_df)-1} turns to finish the exercise")
        print(f"Is the answer correct? {is_correct}")

    logs_by_model_by_level = {}
    if not args.use_prev:
      for level in tqdm(range(game_config.END_LEVEL_BY_GAME[args.game])):
        logs_by_model = {}
        for abbr in abbrs:
          print("#"*10 + f" {abbr} " + "#"*10)
          model = llm_config.MODEL_NAME_BY_ABBR[abbr]
          logs_by_model[model] = communicate.attempt_level_multiple(args.game, model, level, num_trial=num_trial)
        communicate.show_level_trials(abbrs, args.game, level, num_trial, logs_by_model)
        util.save_pkl(logs_by_model, version_dir / f"logs_by_model_level_{level}")
        logs_by_model_by_level[level] = logs_by_model

    if args.use_prev:
      for level in tqdm(range(game_config.END_LEVEL_BY_GAME[args.game])):      
        file = version_dir / f"logs_by_model_level_{level}"
        logs_by_model_by_level[level] = util.load_pkl(file)

    for l, logs_by_model in logs_by_model_by_level.items():
      communicate.show_level_trials(abbrs, args.game, l, num_trial, logs_by_model)
    models = [llm_config.MODEL_NAME_BY_ABBR[a] for a in abbrs]
    eval_plot.plot_results(models, version_dir, args.game)



if __name__ == "__main__":
    main()