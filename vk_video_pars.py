import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
''' Воскресенская солянка '''


def rename_vk_link_to_mobile_vk_link(video_vk_link):
    if ("https://vk.com/video" in video_vk_link and "?z=" not in video_vk_link) or "https://m.vk.com/video" in video_vk_link:
        return video_vk_link.replace('vk.com', 'm.vk.com')
    else:
        m_video_vk_link = ''
        for i in range(video_vk_link.find('z'), len(video_vk_link)):
            m_video_vk_link += video_vk_link[i]

        split_m_video_vk_link = 'https://m.vk.com/'
        for index in m_video_vk_link.split('/'):
            if 'z=video' in index:
                split_m_video_vk_link += index.replace('z=', '')
        return split_m_video_vk_link

#link = rename_vk_link_to_mobile_vk_link(input())
#print('mobile link vk', link)


def create_driver(user_agent):
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument(
        f"user-agent={user_agent}")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--v=99")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
    return driver


def parser_video(user_agent, link):
    driver = create_driver(user_agent)
    link = rename_vk_link_to_mobile_vk_link(link)
    driver.get(link)
    time.sleep(2)
    try:
        video_tag = driver.find_element_by_class_name('VideoPage__video')
        source_arr = video_tag.find_elements_by_tag_name('source')
        links = [elem.get_attribute('src') for elem in source_arr]
        title = driver.find_element_by_class_name(
            'VideoPageInfoRow__title').text
        #print(title, links[0])
        driver.close()
        driver.quit()
        return {'title': title, 'links': links}
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        return "error"
