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

export interface UserRegistrationForm {
    email: string,
    first_name: string,
    last_name: string,
    address: string,
    country: string,
    city: string,
    postal_code: number,
    account_type: string,
    user: {
        username: string,
        password: string
    },
    password2: string
}
