from bs4 import BeautifulSoup
import requests

def get_currency(in_currency,out_currency,in_amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={in_amount}"
    content = requests.get(url).text #this gives the source code of the entire page
    soup = BeautifulSoup(content, 'html.parser')
    rate=soup.find("span",class_="ccOutputRslt").get_text()
    rate = rate[:-4]
    rate = float(rate.replace(",",""))
    return rate

def main ():
    in_cur = input("Enter the 1st currency: ")
    out_cur = input("Enter the 2nd currency: ")
    amt = int(input("enter amount: "))
    rate = get_currency(in_cur,out_cur,amt)
    print(f"{amt} {in_cur} is equal to {rate} {out_cur}")

main()