# -*- coding: utf-8 -*-
import sys

if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO

from PIL import Image

from app.spider.basic_spider import BasicSpider


class UnsensoredSpider(BasicSpider):
    def posterPicture(self, url, r, w, h):
        cropped = None
        try:
            response = self.client_session.get(url)
        except Exception as ex:
            print('error : %s' % repr(ex))
            return cropped

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            # (left, upper, right, lower)
            # cropped = img.crop((0, 0, img.size[0], img.size[1]))

            # 制作最大尺寸背景用白色填充
            w = int(600)
            h = int(1000)
            newim = Image.new('RGB', (w, h), 'black')
            picW, picH = img.size
            newim.paste(img.resize((int(w), int(w / picW * picH))), (0, int((h - w / picW * picH) / 2)))
            cropped = newim
        else:
            pass
        return cropped