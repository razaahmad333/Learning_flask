interface IItem {
  price: number;
  name: string;
}

type ISize = "S" | "L" | "XL";

interface ICloth extends IItem {
  brand: string;
  color: string;
  size: ISize;
}

interface IShirt extends ICloth {
  fullSleeve: boolean;
}

interface IPant extends ICloth {
  tight: boolean;
  elastic: boolean;
}

interface IFood extends IItem {
  isVeg: boolean;
  isSpicy: boolean;
}

type BuyItem = IPant | IShirt | IFood;

interface Customer {
  id: string;
  name: string;
  items?: BuyItem[];
}

interface BillItem {
  name: string;
  price: number;
  discount: number;
  netPrice: number;
}

interface IBill {
  customer: Customer;
  items: BillItem[];
  total: number;
}

interface ISuperMarket {
  title: string;
  items: {
    clothes: Array<IShirt | IPant>;
    foods: IFood[];
  };
  bills?: IBill[];
}

const superMarket: ISuperMarket = {
  title: "BlueRed",
  items: {
    clothes: [
      {
        name: "Denim",
        price: 234,
        fullSleeve: true,
        brand: "Denim",
        color: "Black",
        size: "S",
      },

      {
        name: "Sparky pant",
        price: 234,
        brand: "Sparky",
        elastic: true,
        tight: false,
        color: "Black",
        size: "S",
      },
    ],
    foods: [
      {
        name: "Chowmin",
        price: 100,
        isSpicy: true,
        isVeg: true,
      },
    ],
  },
  bills: [],
};

const arshad: Customer = {
  id: "1",
  name: "Arshad",
};

makeBill({
  customer: arshad,
  items: [
    {
      name: "Chowmin",
      price: 123,
      isSpicy: true,
      isVeg: true,
    },
    {
      name: "Denim",
      price: 2335,
      brand: "Denim",
      fullSleeve: false,
      color: "Black",
      size: "L",
    },
  ],
  market: superMarket,
});

console.log(superMarket.bills);

function BuySomeItem({
  customer,
  items,
}: {
  customer: Customer;
  items: BuyItem[];
}) {
  customer.items = customer.items?.concat(items);
}

function makeBill({
  customer,
  items,
  market,
}: {
  customer: Customer;
  items: BuyItem[];
  market: ISuperMarket;
}) {
  let newBill = {
    customer: customer,
    items: [],
    total: 0,
  } as IBill;
  newBill.customer = customer;
  let currentDiscount: number = 10;
  newBill.total = 0;
  for (let item of items) {
    let netPrice = item.price - (item.price * currentDiscount) / 100;
    newBill.items.push({
      name: item.name,
      price: item.price,
      discount: currentDiscount,
      netPrice,
    });
    newBill.total += netPrice;
  }

  market.bills?.push(newBill);
}
