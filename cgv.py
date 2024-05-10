import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# 현재 날짜, 시간 구하기
now = time.strftime('%Y-$m_%d_%H_%M')
today = time.strftime('%Y%m%d')

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
  try:
    if driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > ul > li:nth-child(2) > a > img').is_displayed():
      print('CGV_02_1 로그인 버튼 노출')
      result_pass_list.append(tc_progress)
      time.sleep(2) # 인터렉션 지연

      try:
        driver.find_element(By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/ul/li[1]/a').click()
        print('CGV_02_2 로그인 버튼 클릭')
        result_pass_list.append(tc_progress)

      except Exception as e:
        fail_reason = '로그인 페이지 진입 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        result_reason_list.append(fail_reason)

  except Exception as e:
    fail_reason = '로그인 버튼 미노출'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_03 로그인 실패
  try: 
    driver.implicitly_wait(10)
    id = driver.find_element(By.ID, 'txtUserId')
    id.click()
    id.send_keys('pso0244')
    print('CGV_03_1 유효하지 않은 아이디 입력')

    failPassword = driver.find_element(By.ID, 'txtPassword')
    failPassword.click()
    failPassword.send_keys('dddd')
    print('CGV_03_2 유효하지 않은 암호')

    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    print('CGV_03_3 [로그인]버튼 클릭')

    time.sleep(2)

    #로그인 실패 오류 컨트롤
    alert = driver.switch_to.alert
    alert.accept()

    # 성공 케이스 추가
    result_pass_list.append(tc_progress)

  except Exception as e:
    fail_reason = '로그인 오류 테스트 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_04 로그인 성공
  try:
    time.sleep(2)
    passId = driver.find_element(By.ID, 'txtUserId')
    passId.clear()
    passId.click()
    passId.send_keys('pso0244')
    print('CGV_04_1 유효한 아이디 입력')

    driver.implicitly_wait(10)
    password = driver.find_element(By.ID, 'txtPassword')
    password.clear()
    password.click()
    password.send_keys('tjsdh316+')
    print('CGV_04_1 유효한 암호 입력')

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    
    driver.implicitly_wait(10)
    if driver.find_element(By.CLASS_NAME, 'logout').is_displayed():
      print('CGV_04 로그인 성공')
      result_pass_list.append(tc_progress)
    else:
      print('로그인 후 메인화면 이동 실패')

  except Exception as e:
    fail_reason = '로그인 성공 테스트 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

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
  try:
    driver.implicitly_wait(10)
    search.click()
    search.send_keys('어벤저스')
    print('CGV_06_1 상영중이지 않은 영화제목 입력')
    driver.find_element(By.ID, 'btn_header_search').click()
    print('CGV_06_2 [돋보기]버튼 클릭')

    driver.implicitly_wait(10)
    if driver.find_element(By.ID, 'search_result').is_displayed():
      print('CGV_06_3 상영중이지 않은 영화 검색 성공')
      result_pass_list.append(tc_progress)
    else:
      print('검색결과 없음 문구 미노출')
  
  except Exception as e:
    print('CGV_06 상영중이지 않은 영화 검색 실패')
    fail_reason = '상영중이지 않은 검색 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #cgv_07 상영중인 검색어 입력 결과 확인
  try:
    driver.implicitly_wait(10)
    search_second = driver.find_element(By.ID, 'header_keyword')
    search_second.click()
    search_second.send_keys('범죄도시4')
    print('CGV_07_1 상영중인 영화제목 입력')
    driver.find_element(By.ID, 'btn_header_search').click()
    print('CGV_07_2 [돋보기]버튼 클릭')
    #검색 결과가 로드될 때까지 명시적으로 대기
    search_success = WebDriverWait(driver, 10).until(
      EC.visibility_of_all_elements_located((By.CLASS_NAME, 'preOrderMovieName'))
    )
    
    if search_success:
      print('CGV_07_3 상영중인 영화 검색 성공')
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
    #cgv_08_1 [예매하기] 버튼 클릭
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, 'btn_style1').click()
    ticket_url = 'http://www.cgv.co.kr/ticket/?MOVIE_CD=20035938&MOVIE_CD_GROUP=20035938'
    print('CGV_08_1 [예매하기]버튼 클릭')

    #cgv_08_2 예매 페이지 진입 확인
    if driver.current_url == ticket_url:
      print('CGV_08_2 예매 페이지 진입 성공')
    else:
      print('CGV_08_2 예매 페이지 진입 실패')

  except Exception as e:
    fail_reason = '예매 진행 영화, 극장선택 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  time.sleep(5)
  try:
    # iframe으로 전환
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'ticket_iframe')))

    # cgv_08_3 상영관 선택
    # JavaScript를 활용해 클릭 강제 실행
    theater_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="theater_area_list"]/ul/li[1]/div/ul/li[2]/a')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", theater_selector)
    driver.execute_script("arguments[0].click();", theater_selector)
    print('CGV_08_3 상영관 선택 성공')

    # cgv_08_4 날짜 선택
    time.sleep(3)
    date_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="date_list"]/ul/div/li[3]/a')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_selector)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(date_selector))
    driver.execute_script("arguments[0].click();", date_selector)
    print('CGV_08_4 날짜 선택 성공')

    # cgv_08_5 시간 선택
    time_selector = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ticket"]/div[2]/div[1]/div[4]/div[2]/div[3]/div[1]/div[1]/ul/li[2]/a')))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(time_selector))
    driver.execute_script("arguments[0].click();", time_selector)
    print('CGV_08_5 날짜 선택 성공')

  except Exception as e:
    fail_reason = f'CGV_08_02 상영관 선택 실패: {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  time.sleep(3)
  # CGV_09 인원/좌석 선택
  try:
    #CGV_09_01 [좌석선택]버튼 클릭
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'tnb_step_btn_right').click()
    print('CGV_09_1 좌석선택 버튼 클릭 성공')

    #CGV_09_02 15세이상 관람 동의 팝업 노출 확인
    driver.implicitly_wait(10)
    pop = driver.find_element(By.CSS_SELECTOR, 'body > div.ft_layer_popup.popup_alert.popup_previewGradeInfo.ko > div.ft > a')

    if pop.is_displayed():
      print('CGV_09_2 15세관람 동의 팝업 노출')
    else:
      print('CGV_09_2 15세관람 동의 팝업 미노출')

    #CGV_09_03 [동의하고 예매하기]버튼 클릭
    driver.implicitly_wait(10)
    pop.click()
    print('CGV_09_3 15세 관람과 동의팝업 클릭')

    #CGV_09_04 일반 [1]인원 클릭
    seat_selector = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//*[@id='nop_group_adult']/ul/li[2]/a"))
    )
    seat_selector.click()
    print('CGV_09_4 일반 1명 선택')

     # "class='no'"이고 텍스트가 "1"인 요소를 클릭합니다.
    element_no_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='no' and text()='1']"))
    )
    if element_no_1.is_displayed():
      element_no_1.click()
    else:
      try: 
      # "class='sreader mod'"의 텍스트가 "선택불가"인지 확인
        current_number = 2
        while current_number <= 16:
          try:
            # "class='sreader mod'" 요소가 "선택불가"인지 확인
                element_sreader_mod = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@class='sreader mod' and text()='선택불가']"))
                )
                # "선택불가" 텍스트가 존재하면 다음 숫자로 이동
                current_number += 1
          except TimeoutException:
                # "선택불가" 텍스트가 없으면, 해당 숫자의 요소를 찾아 클릭하고 루프를 종료
                element_no_next = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//span[@class='no' and text()='{current_number}']"))
                )
                element_no_next.click()
                print(f"Clicked element with class 'no' and text '{current_number}' because it is selectable.")
                break
      except TimeoutException:
        print("Failed to locate element with class 'no' and text '1'.")

    #CGV_09_05 활성된 좌석 클릭
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="seats_list"]/div[1]/div[3]/div[2]/div/div[1]/a').click()
    print('CGV_09_5 활성된 좌석 클릭')

    #CGV_09_06 하단 [결제선택] 버튼 클릭
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#tnb_step_btn_right').click()
    print('CGV_09_6 결제선택 버튼 클릭')

  except Exception as e:
    fail_reason = f'CGV_09 인원/좌석 선택 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  #CGV_10 결제 진행
  try:
    #CGV_10_1 결제수단 신용카드 선택 확인
    driver.implicitly_wait(10)
    if driver.find_element(By.XPATH, "//input[@checked='checked']"):
      print('cgv_10_1 신용카드 체크 확인')
    else:
      print('cgv_10_1 신용카드 체크 미확인')

    #CGV_10_2 카드종류 드롭박스 클릭
    time.sleep(2)
    card_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'lp_card_type')))
    card_list.click()
    print('CGV_10_2 카드종류 드롭박스 클릭')

    #CGV_10_3 BC카드 클릭
    time.sleep(2)
    select_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lp_card_type"]/option[2]')))
    select_card.click()
    print('CGV_10_3 BC카드 클릭')

    #CGV_10_4 하단 [결제하기]버튼 클릭
    payment_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tnb_step_btn_right"]')))
    payment_btn.click()
    print('CGV_10_4  하단 [결제하기]버튼 클릭')
    print('예매내역 확인 팝업 노출 확인')

    time.sleep(3)
    #CGV_10_5 약관동의 체크박스 선택
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'agreementAll').click()
    print('CGV_10_5 약관동의')
    driver.find_element(By.ID, 'resvConfirm').click()
    print('CGV_10_6 결제내용 동의')

    #CGV_10_6 [결제하기]버튼 클릭
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'body > div.ft_layer_popup.popup_reservation_check > div.ft > a.reservation').click()

    time.sleep(5)
    current_url = driver.current_url
    print(current_url)

    # 모든 창 핸들을 가져옵니다.
    all_windows = driver.window_handles
    target_url = "https://ui.vpay.co.kr/web2/qrpay/view?ct=qr&issurCdVal="
    
    for window in all_windows:
    # 각 창으로 전환
      driver.switch_to.window(window)
      # 현재 창의 URL을 확인
      current_url = driver.current_url
      if target_url in current_url:
          print("원하는 URL 창으로 포커스 이동 완료.")
          break

    print(current_url)

    driver.implicitly_wait(10)
    payment_code = driver.find_element(By.CSS_SELECTOR, '#qrCodeNo').text
    input_code = input('결제 코드를 입력해 주세요:')
    #CGV_10_7 [확인]버튼 클릭
    if payment_code == input_code:
      driver.find_element(By.XPATH, '/html/body/article/div/div[2]/div[4]/a').click()
      print('CGV_10_7 [확인]버튼 클릭')
    else:
      input_code = input('결제 코드를 다시 입력해 주세요:')
      driver.find_element(By.XPATH, '/html/body/article/div/div[2]/div[4]/a').click()

  except Exception as e:
    fail_reason = f'CGV_10 결제 진행 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  # CGV_11 예매 확인 (스크린샷)
  time.sleep(5)
  try:
    driver.save_screenshot('screenshot.png')
    print('CGV_11 스크린샷 진행')

  except Exception as e:
    fail_reason = f'CGV_11 스크린샷 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  # CGV_12 메인 화면에서 우상단 [MY CGV]버튼 클릭
  try:
    driver.find_element(By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/h1/a/img').click()

    MY_CGV = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/ul/li[2]/a/img')))
    MY_CGV.click()
    print('CGV_12 [MY CGV]버튼 클릭')

  except Exception as e:
    fail_reason = f'CGV_12 [MY CGV]버튼 클릭 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  # 모든 창 핸들을 가져오기
  all_windows = driver.window_handles
  target_url = "http://www.cgv.co.kr/user/mycgv/reserve/?g=1#contaniner"
  
  for window in all_windows:
  # 각 창으로 전환
    driver.switch_to.window(window)
    # 현재 창의 URL을 확인
    current_url = driver.current_url
    if target_url in current_url:
        print("원하는 URL 창으로 포커스 이동 완료.")
        break

  # CGV_13 [나의 예매내역]버튼 클릭
  try:
    reservation_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/div[1]/div[2]/ul/li[2]/a')))
    reservation_list.click()
    print('CGV_13 [나의 예매내역]버튼 클릭')
  
  except Exception as e:
    fail_reason = f'CGV_13 [나의 예매내역]버튼 클릭 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  # CGV_14 예매 취소
  try:
    cancle_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mycgv_contents > div.cols-mycgv-booking > div.lst-item > div > div.set-btn > div.col-print > button.round.black.cancel')))
    cancle_btn.click()
    print('CGV_14 [예매취소]버튼 클릭')

    alert = driver.switch_to.alert
    alert.accept()
  
  except Exception as e:
    fail_reason = f'CGV_14 [예매취소]버튼 클릭 실패 : {str(e)}'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    result_reason_list.append(fail_reason)

  # CGV_15 로그아웃
  try:
    signout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cgvwrap"]/div[2]/div[1]/div/ul/li[1]/a/img')))
    signout.click()
    print('CGV_15 [로그아웃]버튼 클릭')

  except Exception as e:
    fail_reason = f'CGV_15 [로그아웃]버튼 클릭 실패 : {str(e)}'
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