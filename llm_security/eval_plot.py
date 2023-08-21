import collections

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from llm_security import game_config
from llm_security import util


def plot_results(models, version_dir, game):
  levels = list(range(game_config.END_LEVEL_BY_GAME[game]))
  answers = [game_config.PSW_BY_GAME[game][i + 1] for i in levels]
  successes = collections.defaultdict(int)
  cycles = collections.defaultdict(list)
  cycles_with_win_status = collections.defaultdict(list)  
  for level in levels:
    file = version_dir / f"logs_by_model_level_{level}"
    test = util.load_pkl(file)
    for model, attempts in test.items():
      for df, answer, _ in attempts:
        if (win := answer == answers[level]):
          successes[(model, level)] += 1
          cycles[(model, level)].append(len(df))
        cycles_with_win_status[(model, level)].append((win, len(df) if df is not None else 0)) 
  plot_success_rate(successes, models, levels, version_dir)
  plot_solution_length(cycles, models, levels, version_dir)
  plot_win_loss(cycles_with_win_status, version_dir)


def plot_success_rate(successes, models, levels, version_dir):
  z = 10
  plt.figure(figsize=(z, z/16*9), dpi=300)
  x = np.arange(len(levels))

  bar_width = 0.25

  for model_i in range(len(models)):
    plt.bar(
      x + model_i * bar_width, 
      [successes[(models[model_i], level)] / 20 for level in levels],
      width=bar_width,
      edgecolor='black',
      label=models[model_i],
    )

  plt.grid(True, which='both', linestyle='--', linewidth=0.5)
  plt.ylabel('Success rate')
  plt.xticks(x + bar_width, [f'Level #{i+1}' for i in levels], rotation=45)
  plt.yticks(np.linspace(0, 1, 6))
  plt.ylim(0, 1.3)
  plt.title('Success rate of different models on Bandit levels')
  plt.legend(loc='upper left')
  plt.gca().yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
  plt.savefig(version_dir / "success.png")
  plt.show()


def plot_solution_length(cycles, models, levels, version_dir):
  z = 10
  plt.figure(figsize=(z, z/16*9), dpi=300)
  x = np.arange(len(levels))

  bar_width = 0.25

  for model_i in range(len(models)):
    a = [cycles[(models[model_i], level)] for level in levels]
    y = [np.mean(i) for i in a]
    yerr = [1.96 * np.std(i, ddof=1) / np.sqrt(len(i)) for i in a]
    
    plt.bar(
      x + model_i * bar_width, 
      y,
      yerr=yerr,
      width=bar_width,
      edgecolor='black',
      label=models[model_i],
      capsize=3
    )


  plt.grid(True, which='both', linestyle='--', linewidth=0.5)
  plt.ylabel('Solution length')
  plt.xticks(x + bar_width, [f'Level #{i+1}' for i in levels], rotation=45)
  plt.title('Solution length on Bandit levels')
  plt.legend(loc='upper left')
  plt.savefig(version_dir / "solution_length.png")
  plt.show()  


def plot_win_loss(cycles_with_win_status, version_dir):
  wins = []
  losses = []
  for v in cycles_with_win_status.values():
    wins += [i[1] for i in v if i[0] and i[1] > 0]
    losses += [i[1] for i in v if not i[0] and i[1] > 0]  
  z = 10
  fig, ax = plt.subplots(1, 2, figsize=(z, z/16*9), dpi=300)  # 1 row, 2 columns of axes

  # Plot data on the first axis
  ax[0].hist(wins, bins=31, range=(0, 31), color='blue', edgecolor='black')
  ax[0].set_title('Length of successful attempts')
  ax[0].set_xlabel('Attempt length')

  # Plot data on the second axis
  ax[1].hist(losses, bins=31, range=(0, 31), color='red', edgecolor='black')
  ax[1].set_title('Length of failed attempts')
  ax[1].set_xlabel('Attempt length')
  plt.tight_layout()  # Adjust layout to prevent overlaps
  plt.savefig(version_dir / "win_loss.png")
  plt.show()
