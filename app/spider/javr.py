# -*- coding: utf-8 -*-
import re

from app.spider.uncensored_spider import UnsensoredSpider


class Javr(UnsensoredSpider):

    def search(self, q):

        '''
        执行查询函数
        '''
        item = []
        '获取查询结果页html对象'
        url = 'https://javr.club/?s=%s' % q
        xpathResult = "//*[@id='cactus-body-container']/div/div/div/div[2]/div/div[6]/div/div[2]/article[1]/div/div[2]/h3/a"
        html_item = self.getHtmlByurl(url)
        if not html_item['issuccess']:
            return item

        resultName = html_item['html'].xpath(xpathResult)
        if resultName is None:
            return item
        if len(resultName) == 0:
            return item
        if re.search(q, resultName[0].text, re.IGNORECASE):
            resultUrl = html_item['html'].xpath(xpathResult)[0].attrib['href']
            html_item = self.getHtmlByurl(resultUrl)
            if html_item['issuccess']:
                media_item = self.analysisMediaHtmlByxpath(
                    html_item['html'], q)
                item.append({'issuccess': True, 'data': media_item})
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
        media = self.media.copy()
        number = self.tools.cleanstr(q.upper())
        media.update({'m_number': number})

        xpath_title = "//*[@id=\"cactus-body-container\"]/div/div/div/div[2]/div/div[2]/article/div[3]/h1"
        title = html.xpath(xpath_title)[0].text
        title = title.replace('Watch XXX Japanese Porn -', '')
        media.update({'m_title': title})
        media.update({'m_summary': title})
        xpath_poster = '//*[@id="my-cover"]'
        post_url = html.xpath(xpath_poster)[1].attrib['src']
        media.update({'m_poster': post_url})
        media.update({'m_art_url': post_url})

        xpath_studio = '//*[@id="cactus-body-container"]/div/div/div/div[2]/div/div[2]/article/div[3]/div[1]/div/p[3]/a'
        if len(html.xpath(xpath_studio)) >0 :
            studio = html.xpath(xpath_studio)[0].text
            media.update({'m_studio': studio})

        directors = ''
        media.update({'m_directors': directors})

        xpath_category = "//*[@id=\"cactus-body-container\"]/div/div/div/div[2]/div/div[2]/article/div[3]/div[1]/div/div[2]/div/div/a"
        categorys = html.xpath(xpath_category)
        category_list = []
        for category in categorys:
            category_list.append(self.tools.cleanstr(category.text))
        categorys = ','.join(category_list)
        if len(categorys) > 0:
            media.update({'m_category': categorys})

        xpath_actor_name = "//*[@id=\"cactus-body-container\"]/div/div/div/div[2]/div/div[2]/article/div[4]/div/div[2]/a/p/span"
        if len(html.xpath(xpath_actor_name)) > 0:
            actor_name = html.xpath(xpath_actor_name)[0].text
            xpath_actor_pic = '//*[@id="cactus-body-container"]/div/div/div/div[2]/div/div[2]/article/div[4]/div/div[1]/a/img'
            actor_url = html.xpath(xpath_actor_pic)[0].attrib['data-src']
            media.update({'m_actor': {actor_name: actor_url}})
        return media
