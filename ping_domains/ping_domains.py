import csv
import os


def main():
    domains = ["yandex.ru", "NSU.ru", "google.ru", "vk.com", "mail.google.com", "mechhub.ru", "youtube.com", "mail.ru", "twitch.tv", "github.com"]

    from ping3 import ping

    results = []

    for domain in domains:
        response_time = ping(domain)
        results.append({"Domain": domain, "ResponseTime": response_time})

    with open("ping_results.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Domain", "ResponseTime"])
        writer.writeheader()
        for result in results:
            writer.writerow(result)

if __name__ == '__main__':
    main()