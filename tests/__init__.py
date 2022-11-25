from pathlib import Path
import sys

PROJECT_PATH = Path(__file__).parents[1]
print(PROJECT_PATH)
SOURCE_PATH = PROJECT_PATH / 'src'
sys.path.append(SOURCE_PATH)