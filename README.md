# VK Video Downloader

## Настройка установки

## FastAPI
```bash
$ pip install -r ./requirements.txt
$ uvicorn main:app
```

## Vue
```bash
$ cd frontend
$ npm install
$ npm run serve
```
Для работы сервиса нужен браузер Google Chrome и chromedriver
```bash
#vk_video_pars.py
driver = webdriver.Chrome(
    executable_path='Укажите тут путь к chromedriver', chrome_options=options)
```