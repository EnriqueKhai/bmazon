interface Product_base {
    product_id: number,
    prod_name: string,
    prod_desc?: string
    price: number,
    prod_discount?: number,
    prod_image: string
}

export interface Product extends Product_base {
    supplier: number,
    category: number
}