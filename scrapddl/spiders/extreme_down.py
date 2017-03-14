from base import BaseSpider


class EDBaseSpider(BaseSpider):
    main_attr_html = 'a'
    main_class = 'top-last thumbnails'
    domain = 'https://www.extreme-down.in'

    def _get_page_url(self, element):
        return element.items()[1][1]

    def _get_title(self, element):
        return element.xpath(
            ".//span[@class='top-title']")[0].text.strip()

    def _get_genre(self, element):
        return element.xpath(
            ".//span[@class='top-genre']")[0].text.strip()

    def _get_image(self, element):
        return element.xpath(".//img/@src")[0]

    def _get_quality_language(self, element):
        return element.xpath(
            ".//span[@class='top-lasttitle']")[0].text.strip()


class EDMoviesSpider(EDBaseSpider):
    urls = ['/films-sd/', '/films-hd/']


class EDTvShowsSpider(EDBaseSpider):
    urls = ['/series/vostfr/']