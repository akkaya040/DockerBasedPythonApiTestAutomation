const express = require('express');
const app = express();
const port = 8080;

const products = [
  {
    "id": 1,
    "title": "Apple iPad 9. Nesil 64 GB",
    "description": "Lorem ipsum dolor sit amet.",
    "price": 5400,
    "isBasketDiscount": true,
    "basketDiscountPercentage": 10,
    "rating": 4.69,
    "stock": 50,
    "isActive": false,
    "brand": "Apple",
    "category": "ipad",
    "images": [
      "https://cdn.dsmcdn.com/ty321/product/media/images/20220204/14/43694637/262004743/1/1_org_zoom.jpg",
      "https://cdn.dsmcdn.com/ty323/product/media/images/20220204/14/43694637/262004743/3/3_org_zoom.jpg"
    ]
  },
  {
    "id": 2,
    "title": "Apple iPhone 12 64 GB",
    "description": "Lorem ipsum dolor sit amet.",
    "price": 13500,
    "isBasketDiscount": false,
    "rating": 4.4,
    "stock": 20,
    "brand": "Apple",
    "category": "smartphones",
    "images": [
      "https://cdn.dsmcdn.com/mnresize/1200/1800/ty94/product/media/images/20210404/09/74346117/57616583/1/1_org_zoom.jpg"
    ]
  }
];

app.get('/product', (req, res) => {
  const scenario = req.query.scenario || 'default';

  if (scenario === 'unauthorized') {
    res.status(401).json({ message: 'Unauthorized' });
  } else if (scenario === 'serviceUnavailable') {
    res.status(503).json({ message: 'Service Unavailable' });
  } else {
    res.status(200).json(products);
  }
});

app.listen(port, () => {
  console.log(`Mock API server is running on port ${port}`);
});
