# 대상을 찾고 -> 상태를 체크하고 -> 흐름을 제어 -> 액션을 전달
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException



# 현재 날짜, 시간 구하기
now = time.strftime('%Y-$m_%d_%H_%M')

result_pass_list = [] #pass한 TC ID를 가지고 있는 리스트
result_fail_list = [] #fail한 TC ID를 가지고 있는 리스트
result_reason_list = [] #fail한 원인을 가지고 있는 리스트
tc_count = 15 #전체 TC 개수 카운트

# 테스트 전 과정에 걸쳐 에러발생 시 에러기록하는 try, except문 
# f = open(f'test_result/{now}_test_result.txt', 'w')
# f.write(f'테스트 수행 일자 - {now}\n')

try: 

  # TC cgv_01 cgv 홈페이지 접속 
  tc_progress = 'cgv_01'
  driver = webdriver.Chrome()
  driver.get('https://www.cgv.co.kr')
  driver.implicitly_wait(10)
  driver.maximize_window()
  print('##################테스트 시작###################')
  print('CGV_01 cgv홈페이지 접속 성공')
  print(driver.title)
  print(driver.current_url)
  

  # TC cgv_02 로그인 버튼 확인, 클릭
  # try:
  #   if driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > ul > li:nth-child(2) > a > img').is_displayed():
  #     print('CGV_02_1 로그인 버튼 노출')
  #     result_pass_list.append(tc_progress)
  #     time.sleep(2) # 인터렉션 지연

  #     try:
  #       driver.find_element(By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/ul/li[1]/a').click()
  #       print('CGV_02_2 로그인 버튼 클릭')
  #       result_pass_list.append(tc_progress)
  #       time.sleep(5)

  #     except Exception as e:
  #       fail_reason = '로그인 페이지 진입 실패'
  #       print(fail_reason)
  #       result_fail_list.append(tc_progress)
  #       result_reason_list.append(fail_reason)

  # except Exception as e:
  #   fail_reason = '로그인 버튼 미노출'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   result_reason_list.append(fail_reason)

  #cgv_03 로그인 실패
  # try: 
  #   driver.implicitly_wait(10)
  #   id = driver.find_element(By.ID, 'txtUserId')
  #   id.click()
  #   id.send_keys('pso0244')

  #   failPassword = driver.find_element(By.ID, 'txtPassword')
  #   failPassword.click()
  #   failPassword.send_keys('dddd')

  #   driver.find_element(By.XPATH, '//*[@id="submit"]').click()
  #   time.sleep(2)

  #   #로그인 실패 오류 컨트롤
  #   alert = driver.switch_to.alert
  #   alert.accept()

  #   print('CGV_03 로그인 실패')
  #   result_pass_list.append(tc_progress)

  # except Exception as e:
  #   fail_reason = '로그인 오류 테스트 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   result_reason_list.append(fail_reason)

  #cgv_04 로그인 성공
  # try:
  #   time.sleep(2)
  #   passId = driver.find_element(By.ID, 'txtUserId')
  #   passId.clear()
  #   passId.click()
  #   passId.send_keys('pso0244')

  #   driver.implicitly_wait(10)
  #   password = driver.find_element(By.ID, 'txtPassword')
  #   password.clear()
  #   password.click()
  #   password.send_keys('tjsdh316+')

  #   time.sleep(2)
  #   driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    
  #   driver.implicitly_wait(10)
  #   if driver.find_element(By.CLASS_NAME, 'logout').is_displayed():
  #     print('CGV_04 로그인 성공')
  #     result_pass_list.append(tc_progress)
  #   else:
  #     print('로그인 후 메인화면 이동 실패')

  # except Exception as e:
  #   fail_reason = '로그인 성공 테스트 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   result_reason_list.append(fail_reason)

  #cgv_05 검색 입력란 노출 확인
  driver.implicitly_wait(10)
  search = driver.find_element(By.ID, 'header_keyword')
  
  if search.is_displayed():
    print('CGV_05 검색어 입력란 노출 확인')
    result_pass_list.append(tc_progress)

  else:
    print('CGV_05 검색어 입력란 노출 실패')
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_06 상영중이지 않은 검색어 입력 결과 확인
  # try:
  #   driver.implicitly_wait(10)
  #   search.click()
  #   search.send_keys('어벤저스')
  #   driver.find_element(By.ID, 'btn_header_search').click()

  #   driver.implicitly_wait(10)
  #   if driver.find_element(By.ID, 'search_result').is_displayed():
  #     print('CGV_06 상영중이지 않은 영화 검색 성공')
  #     result_pass_list.append(tc_progress)
  #   else:
  #     print('검색결과 없음 문구 미노출')
  
  # except Exception as e:
  #   print('CGV_06 상영중이지 않은 영화 검색 실패')
  #   fail_reason = '상영중이지 않은 검색 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   result_reason_list.append(fail_reason)

  #cgv_07 상영중인 검색어 입력 결과 확인
  
  try:
    driver.implicitly_wait(10)
    search_second = driver.find_element(By.ID, 'header_keyword')
    search_second.click()
    search_second.send_keys('범죄도시4')
    driver.find_element(By.ID, 'btn_header_search').click()
    
    #검색 결과가 로드될 때까지 명시적으로 대기
    search_success = WebDriverWait(driver, 10).until(
      EC.visibility_of_all_elements_located((By.CLASS_NAME, 'preOrderMovieName'))
    )
    
    if search_success:
      print('CGV_07 상영중인 영화 검색 성공')
      result_pass_list.append(tc_progress)
    else:
      print('검색결과 없음 문구 미노출')
  
  except Exception as e:
    print('CGV_07 상영중인 영화 검색 실패')
    fail_reason = '상영중인 영화 검색 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_08 예매하기 극장, 날짜 선택
  try:
    #cgv_08_1 예매하기 버튼 클릭
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, 'btn_style1').click()
    ticket_url = 'http://www.cgv.co.kr/ticket/?MOVIE_CD=20035938&MOVIE_CD_GROUP=20035938'

    if driver.current_url == ticket_url:
      print('CGV_08_1 예매 페이지 진입 성공')
    else:
      print('CGV_08_1 예매 페이지 진입 실패')

  except Exception as e:
    fail_reason = '예매 진행 영화, 극장선택 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  time.sleep(5)
  try:
     # iframe으로 전환
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'ticket_iframe')))

    # 상영관 선택
    # JavaScript를 활용해 클릭 강제 실행
    theater_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="theater_area_list"]/ul/li[2]/div/ul/li[7]/a')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", theater_selector)
    driver.execute_script("arguments[0].click();", theater_selector)
    print('CGV_08_05 상영관 선택 성공')

    # 날짜 선택
    time.sleep(3)
    date_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="date_list"]/ul/div/li[3]/a')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_selector)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(date_selector))
    driver.execute_script("arguments[0].click();", date_selector)
    print('CGV_08_06 날짜 선택 성공')

    # 시간 선택
    time_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ticket"]/div[2]/div[1]/div[4]/div[2]/div[3]/div[1]/div[1]/ul/li[2]/a')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(time_selector))
    driver.execute_script("arguments[0].click();", time_selector)
    print('CGV_08_07 날짜 선택 성공')


  except Exception as e:
    fail_reason = f'CGV_08_02 상영관 선택 실패: {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)
  
  time.sleep(20)

except Exception as e:
  print('에러가 발생하여 테스트 종료:', e)
  driver.quit()
  sys.exit(1)

finally:
  print('##########테스트 스크립트 종료##########')
  driver.quit()