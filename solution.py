import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 82953459 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    alpha = 1 - p
    stat = np.square(x).sum()
    
    left_bound = np.sqrt(stat / (62 * chi2.ppf(1 - alpha / 2, 2 * len(x))))
    right_bound = np.sqrt(stat / (62 * chi2.ppf(alpha / 2, 2 * len(x))))
            
    return left_bound, right_bound
