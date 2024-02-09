import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top bid']['price'],quote['top_ask']['price'],(quote['top bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top bid']['price'],quote['top_ask']['price'],(quote['top bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_aBigger(self):
     prices=[[34.4,12.67],[556.7,234.99]]
     for stocks in prices:
        self.assertEqual(getRatio(stocks[0],stocks[1]),stocks[0]/stocks[1])

  def test_getRatio_aSmaller(self):
     prices=[[23.4,66.5],[345.6,555.3]]
     for stocks in prices:
        self.assertEqual(getRatio(stocks[0],stocks[1]),stocks[0]/stocks[1])
  
  def test_getRatio_zeros(self):
     prices=[[0,6],[6,0]]
     for stocks in prices:
        self.assertEqual(getRatio(stocks[0],stocks[1]),stocks[0]/stocks[1])



if __name__ == '__main__':
    unittest.main()
