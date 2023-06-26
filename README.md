# Amazon Review Scraper and AI review summerize and rate products

this program takes your amazon search query and gathers all the asins(products) from the first page of results (26ish)
it then goes to each products page and downloads all the reviews(top 100 recent and top 100 relevant)
it then takes all those reviews and uses ai to summaries the reviews and rank the product based on your key qualities you are interested in

Bones found here [ScrapeHero Tutorials](https://www.scrapehero.com/how-to-scrape-amazon-product-reviews/)

## Usage

1. Install Requirements `pip3 install -r requirements.txt`
2. create account with openia and save your api key
3. Add Amazon Search Query
4. Add Key features your interested in
5. Run `python3 reviews.py`

## Example Data Format when providing the search text and key features im looking for

https://www.amazon.com/dp/B0C2HQFVVR Mixed reviews. Some say it cools well and is quiet while others say it is loud and inefficient. Price varies.

https://www.amazon.com/dp/B091CHK173 Midea portable air conditioner is efficient and effective in cooling large rooms, but can be noisy. The product can be easily set up but has some issues with its build quality and design. Some customers also have issues with the delivery time and the hose that comes with the product. Overall, the product is good for those looking for an energy-efficient air conditioner with dual hose design and smart features. However, some may find it noisy and lacking in some design features. Noise level: Varies. Size: Good for large rooms. Price: Affordable to expensive depending on model.

https://www.amazon.com/dp/B01DLPUWG2 A Portable AC with a powerful cooling effect that can cool a room of almost any size quickly, but can be a bit noisy on the highest fan setting. Installation can have some quirks but is simple with a little improvisation. The unit looks nice, and even with the largest version, it only cools one room. It is reasonably priced and straightforward to use. The noise level can be a potential annoyance, but it could appeal to those who prefer some background noise to sleep. Our overall rating for the product is noise level: moderate, size: compact, price: reasonable.

https://www.amazon.com/dp/B0BV98JPFT The 90° Oscillated Evaporative Portable Air Conditioner is compact, efficient and operates quietly. It has a built-in humidifier, five wind speeds, and a gradient light. It cools small rooms quickly and is easy to use. Some reviews mention the bright display and recommend against using it at night. Overall, the product has a high rating for noise level, size, and price.

https://www.amazon.com/dp/B07DQVNSP8 The SereneLife portable air conditioner cools well, but the noise level varies. Setup is easy, and size is compact. The price is reasonable, but some issues might arise with the exhaust and drainage. Overall, it is a reliable and portable cooling solution. Quality rating: noise level - average, size - good, price - good.

https://www.amazon.com/dp/B0C893DF85 The AC unit is compact, efficient, and comes with a remote control and app. It cools the room quickly and works well even with limited window options. The noise level is a bit high but manageable. The price and design were praised by users. Overall rating: noise level 7/10, size 9/10, price 8/10.

https://www.amazon.com/dp/B0C2HQFVVR Most reviews comment on the noise level, with some finding it too loud. There are mixed reviews on the cooling efficiency, with some finding it to be very effective and others disappointed. The size is generally considered reasonable, although some buyers were surprised by the weight. The price is also mixed, with some saying it's not worth it. Overall, it seems like a decent portable AC unit.

https://www.amazon.com/dp/B01DLPUWL2 The Portable AC unit cools rooms efficiently, but noise levels vary, with some finding it loud and others accepting it as white noise. Installation is easy but the window kit could be improved. The unit has been effective in cooling rooms of various sizes and has been a good investment for those in hot climates. However, some found the display too bright and the hose can get hot. The price is considered fair. Overall, the performance of the AC unit is good, but noise level may vary. Rating: 

https://www.amazon.com/dp/B07HR5CN7G Summary: Mixed reviews on noise level, size, and price, with some customers finding it too loud but others satisfied with its cooling capabilities. The unit is generally effective

https://www.amazon.com/dp/B0B425VKMS The AC unit is generally efficient but has some installation issues. It can be noisy, but on the whole, it works well in cooling rooms. Rating: noise level - 3/5, size - 4/5, price - 4/5.

https://www.amazon.com/dp/B0BXX35WDB Summary: The product is praised for its quiet operation, compact size, and multiple functions. It is useful for cooling small spaces and providing relief from heat. Its noise level and size are highly rated, but some customers note that it could be more powerful. Overall, the product is recommended for its effectiveness and reasonable price. 



