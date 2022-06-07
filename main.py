from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from vk_video_pars import parser_video
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Parser vk-video")
# Если запущен dev-server vue, эти строки нужно расскоментировать
""" app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) """

@app.get(
    "/link_vk",
    response_description="Получение видео по ссылке и user-agent",
)
async def link_vk(link, user_agent):
    link = parser_video(user_agent, link)
    if link == "error":
        raise HTTPException(404, "Ошибка при получении видео: возможно видео не существует или оно скрыто настройками приватности.")
    if len(link['links']) == 6:
        return {'title': link['title'], 'video': link['links'][0]}
    else:
        if len(link['links']) == 8:
            return {'title': link['title'], 'video': link['links'][2]}
        elif len(link['links']) == 7:
            return {'title': link['title'], 'video': link['links'][1]}
        return {'title': link['title'], 'video': link['links'][0]}
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/", StaticFiles(directory="static",html = True), name="static")