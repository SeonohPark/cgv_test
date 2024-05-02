from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 현재 날짜, 시간 구하기
now = time.strftime('%Y-$m_%d_%H_%M')

result_pass_list = [] #pass한 TC ID를 가지고 있는 리스트
result_fail_list = [] #fail한 TC ID를 가지고 있는 리스트
result_reason_list = [] #fail한 원인을 가지고 있는 리스트
tc_count = 15 #전체 TC 개수 카운트

# 테스트 전 과정에 걸쳐 에러발생 시 에러기록하는 try, except문 
try:
  # f = open(f'test_result/{now}_test_result.txt', 'w')
  # f.write(f'테스트 수행 일자 - {now}\n')

  # TC cgv_01 cgv 홈페이지 접속 
  tc_progress = 'cgv_01'
  driver = webdriver.Chrome()
  driver.get('https://www.cgv.co.kr')
  driver.implicitly_wait(10)
  driver.maximize_window()

 

except Exception as e:
  print('에러 발생하여 테스트 스크립트 종료.')
