# -*- coding: utf-8 -*-
from app.spider.uncensored_spider import UnsensoredSpider
from app.internel.browser_tools import BrowserTools
from PIL import Image
import sys
if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO


class MGSBlogg(UnsensoredSpider):

    def search(self, q):
        '''
        执行查询函数
        '''
        item = []

        '获取查询结果列表页html对象'
        url = 'http://mgs.blogg.org/search?q=%s' % q
        list_html_item = self.getHtmlByurl(url)
        if list_html_item['issuccess']:

            xpaths = "//div[@class='module_titre']/h1/a/@href"
            page_url_list = self.getitemspage(
                list_html_item['html'], xpaths)

            for page_url in page_url_list:
                if page_url != '':
                    html_item = self.getHtmlByurl(
                        'http://mgs.blogg.org%s' % page_url)
                    if html_item['issuccess']:
                        media_item = self.analysisMediaHtmlByxpath(
                            html_item['html'], q)
                        item.append({'issuccess': True, 'data': media_item})
                break
        else:
            pass  # print repr(html_item['ex'])

        return item

    def analysisMediaHtmlByxpath(self, html, q):
        """
        根据html对象与xpath解析数据
        html:<object>
        html_xpath_dict:<dict>
        return:<dict{issuccess,ex,dict}>
        """

        '''
        xpath_number = "//div[@class='col-md-3 info']/p[1]/span[2]/text()"
        number = html.xpath(xpath_number)
        if len(number) > 0:
            number = self.tools.cleanstr(number[0])
            self.media.update({'m_number': number})
        '''
#//div[@class='article_text']/p/a/@href  海报

#//div[@class='article_text']/p/text()  信息：      
# 

        media = self.media.copy()

        info_list = []
        xpath_infos = "//div[@class='article_text']/p/text()"
        infos = html.xpath(xpath_infos)
        for item in infos: 
            tmp = item.split('：')
            info_list.append(tmp)
        for info in info_list:
            if info[0].replace(' ','') == '品番':#番号
                media.update({'m_number': self.tools.cleanstr(info[1])})

            elif info[0].replace(' ','') =='配信開始日':#日期
                media.update({'m_year': self.tools.cleanstr(info[1])})      

            elif info[0].replace(' ','') =='メーカー':#工作室
                media.update({'m_studio': self.tools.cleanstr(info[1])})     
                
            elif info[0].replace(' ','') =='シリーズ':#系列
                if info[1].replace(' ','') == '':
                    pass
                else:
                    media.update({'m_collections': self.tools.cleanstr(info[1])})

            elif info[0].replace(' ','') =='ジャンル':#类型                
                tmp_list = info[1].split(' ')
                while '' in tmp_list:
                    tmp_list.remove('')
                categorys = tmp_list
                category_list = []
                for category in categorys:
                    category_list.append(self.tools.cleanstr(category))
                categorys = ','.join(category_list)
                if len(categorys) > 0:
                    media.update({'m_category': categorys})
                    
            elif info[0].replace(' ','') =='出演':#演员                
                actor = {}
                actor_name = info[1].replace(' ','')                
                if len(actor_name) > 0:
                    actor.update({self.tools.cleanstr(info[1]): ''})
                    media.update({'m_actor': actor})
            else:
                pass        


        xpath_title = "//div[@class='module_titre']/h1/text()"
        title = html.xpath(xpath_title)
        if len(title) > 0:
            title = self.tools.cleanstr(title[0].replace(media['m_number'],''))
            media.update({'m_title': title})

        
        xpath_poster = "//div[@class='article_text']/p[1]/a/@href"
        poster = html.xpath(xpath_poster)
        if len(poster) > 0:
            poster = self.tools.cleanstr(poster[0])
            media.update({'m_poster': poster})
            media.update({'m_art_url': poster})

        return media
