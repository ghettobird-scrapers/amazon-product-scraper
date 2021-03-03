
#Based on:
#https://github.com/drawrowfly/amazon-product-api
from ghettobird import fly
from pprint import pprint

#Once the element is located via xpath, a 'transformer' function is expected to return a string
#Data can be cleaned like this or in a more traditional way
def TRANSFORM_get_all_text (element):
    split = element.text_content()
    split = split.split('Amazon Best Sellers Rank')
    split = split[1].split('(See')
    return split[0]

bird = {
 "url": "https://www.amazon.com/dp/B086XMXYTR",
    "flightpath": {
        "product_name": "//span[@id='productTitle']",
        "price": "//span[@id='priceblock_ourprice']",
        "description_bullets": ["//div[@id='feature-bullets']//span[@class='a-list-item']"],
        "description": "//div[@id='productDescription']//p",
        "package_dimensions": "//div[@id='detailBullets_feature_div']//span[@class='a-text-bold' and contains(text(),'Package Dimensions')]/following-sibling::*[1]",
        "department": "//div[@id='detailBullets_feature_div']//span[@class='a-text-bold' and contains(text(),'Department')]/following-sibling::*[1]",
        "date_first_available": "//div[@id='detailBullets_feature_div']//span[@class='a-text-bold' and contains(text(),'Date First Available')]/following-sibling::*[1]",
        "manufacturer": "//div[@id='detailBullets_feature_div']//span[@class='a-text-bold' and contains(text(),'Manufacturer')]/following-sibling::*[1]",
        "asin": "//div[@id='detailBullets_feature_div']//span[@class='a-text-bold' and contains(text(),'ASIN')]/following-sibling::*[1]",
        "sales_rank": {
            "path": "//*[@id='SalesRank']",
            "@transformer": TRANSFORM_get_all_text
        },
        "customer_rating": "//i[@class='a-icon a-icon-star a-star-4-5']//span"
    }
}

scraped = fly(bird)
pprint(scraped['results'])

