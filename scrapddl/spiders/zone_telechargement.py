from base import BaseSpider


class ZTBaseSider(BaseSpider):
    main_attr_html = 'div'
    main_class = 'cover_global'
    domain = "https://zone-telechargement.ws"

    def _get_page_url(self, element):
        return element.xpath(
            ".//div[@class='cover_infos_title']/a")[0].items()[0][1]

    def _get_title(self, element):
        return element.xpath(
            ".//div[@class='cover_infos_title']/a")[0].text.strip()

    def _get_genre(self, element):
        return None

    def _get_image(self, element):
        image = element.xpath(".//img/@src")[0]
        if not self.is_absolute(image):
            return "{}{}".format(self.domain, image)
        return image

    def _get_quality_language(self, element):
        return element.xpath(
            ".//div[@class='cover_infos_title']/span/span/b")[0].text.strip()


class ZTMoviesSpider(ZTBaseSider):
    urls = ['/nouveaute/', '/films-bluray-hd/']


class ZTTvShowsSpider(ZTBaseSider):
    urls = ['/series-vostfr/']