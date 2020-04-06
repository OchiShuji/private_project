import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#import numpy as np 

flg = int(input("difficulty?(1.easy/2.normal/3.hard)\n>> "))

driver = webdriver.Chrome()
driver.maximize_window()

if flg == 1:
    driver.get("http://kakigoori.or.jp/kentei/easy")
    difficulty = "easy"
elif flg == 2:
    driver.get("http://kakigoori.or.jp/kentei/normal")
    difficulty = "normal"
elif flg == 3:
    driver.get("http://kakigoori.or.jp/kentei/hard")
    difficulty = "hard"
else:
    raise Exception("不正な入力")

max_q = 8
answers = [1] * max_q
score = []

def create_xpath(d,q_num,ans):
    '''xpathを生成する'''
    xpath = "//*[@id='kentei" + d + "']/fieldset/div[{}]/div/div/div/div/div/label[{}]".format(q_num,ans)
    return xpath

def click_choice(driver,xpath):
    '''選択肢を選択'''
    time.sleep(0.5)
    choice = driver.find_element_by_xpath(xpath)
    choice.click()

def submit_ans(driver,d):
    '''答案を提出'''
    submission = driver.find_element_by_xpath("//*[@id='kentei"+ d +"']/fieldset/div[9]/div[2]/input")
    time.sleep(1)
    if submission.is_displayed():
        submission.click()
    else:
        raise Exception("全問に解答されていません")

def get_result(driver):
    '''結果を取得'''
    result_path = driver.find_element_by_xpath("/html/body/div[2]/main/article/section/section[1]/div[1]/div[2]/p[1]/span[3]")
    result = result_path.text
    return(int(result))

def retry(driver):
    '''再挑戦する'''
    time.sleep(1)
    button = driver.find_element_by_xpath("/html/body/div[2]/main/article/section/section[1]/div[1]/div[2]/div/a")
    button.click()

#解答
n = 0
q = 0
while True:
    print(score)
    print("n=",n,"q=",q)
    for i in range(0,len(answers)):
        path = create_xpath(difficulty,i+1,answers[i])
        click_choice(driver,path)
    submit_ans(driver,difficulty)
    score.append(get_result(driver))
    if n == 0:
        answers_prev = answers.copy()
        answers[q] = answers[q] + 1
        retry(driver)
    elif score[n] > score[n-1]:
        if score[n] == max_q - 1:
            #7問正解で強制的に合格になってしまう
            print("合格しました。おめでとうございます。\n試行回数は{}回です。".format(n+1))
            break
        else:
            q = q + 1
            answers_prev = answers.copy()
            answers[q] = answers[q] + 1
            retry(driver)
    elif score[n] < score[n-1]:
        answers_prev = answers.copy()
        answers[q] = answers[q] - 1
        retry(driver)
    else:
        answers_prev = answers.copy()
        answers[q] = answers[q] + 1
        retry(driver)
    n = n + 1










