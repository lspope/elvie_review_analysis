from bs4 import BeautifulSoup
import requests
import json
import csv



def add_reviews_to_collection(reviews):
    for review in reviews:
        review_dict = {}

        unique_id = review.find("article", class_="review")["id"]
        review_dict["id"] = unique_id

        star_rating = review.find("div", class_="star-rating star-rating--medium").img["alt"].strip()
        review_dict["star_rating"] = star_rating

        location = review.find("div", class_="consumer-information__location").find("span").text.strip()
        review_dict["location"] = location

        datetime_string = review.find("div", class_="review-content-header__dates").find("script").string
        datetime_json = json.loads(datetime_string)
        datetime = datetime_json["publishedDate"]
        review_dict["datetime"] = datetime

        content = review.find("div", class_="review-content__body").text.replace("\n", " ").strip()
        review_dict["content"] = content
    
        review_collection.append(review_dict)
   

def scrape_page(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    # get the next page url
    nav_next = soup.find("nav", class_="pagination-container AjaxPager")
    next_page_link = nav_next.find("a", class_="button button--primary next-page")
    next_page_url = prefix + next_page_link["href"]
    print(next_page_url)

    # get the reviews on the current page
    reviews = soup.find_all("div", class_="review-card")
    print(len(reviews))
    add_reviews_to_collection(reviews)
    return next_page_url


if __name__ == "__main__":
    review_collection = []
    start_url = "https://uk.trustpilot.com/review/www.elvie.com"
    prefix = "https://uk.trustpilot.com"
    numpages = 74

    # scrape reviews from the first page
    next_url = scrape_page(start_url)

    # now scrape reviews from the following pages 
    for i in range(numpages):
        next_url = scrape_page(next_url)

    keys = review_collection[0].keys()
    with open('./data/elvie_trustpilot_reviews.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(review_collection)

    print(f"fetched {len(review_collection)} reviews")
    print(f"Wrote reviews to csv file")