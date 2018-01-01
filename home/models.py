from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    # Masthead 刊頭
    background-image = 
    masthead-img = 
    masthead-title = 
    masthead-subtitle = 
    
    # About Section 關於我們
    img-fluid = 
    introduction =

    # About Team 這裡有三個人皆有人名\大頭貼\專長 用以介紹團隊 團隊部分另開資料表


    # Services Section 服務項目 有一個頭標及二個產品的介紹 產品部分另開資料表

    # Contact Section 

    # 使用客戶 此部分另開資料表

    # 購買連結 刪除

    # Footer

