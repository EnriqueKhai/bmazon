import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../../interfaces';

// HTTP configurations.
const HTTP_OPTIONS = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
  })
};

// CRUD URLs.
const GET_LISTING_DETAIL_URL: string  = "http://localhost:8000/api/products/?product_id=";
const GET_ALL_LISTINGS_URL: string    = "http://localhost:8000/api/products";
const CREATE_NEW_LISTING_URL: string  = "http://localhost:8000/api/products/new";
const EDIT_LISTING_DETAIL_URL: string = "http://localhost:8000/api/products";
const DELETE_LISTING_URL: string      = "http://localhost:8000/api/products";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(
    private http: HttpClient
  ) { }

  private product_to_JSON(listing_product: Product) {
    let listing_JSON = {
      "prod_name"    : listing_product.prod_name,
      "prod_desc"    : listing_product.prod_desc,
      "price"        : listing_product.price,
      "prod_discount": listing_product.prod_discount,
      "supplier"     : listing_product.supplier,
      "category"     : listing_product.category
    }
    return listing_JSON;
  }

  get_listing_by_ID(listing_id: string): Observable<Product> {
    return this.http.get<Product>(GET_LISTING_DETAIL_URL + listing_id);
  }

  get_all_listings(): Observable<Product[]> {
    return this.http.get<Product[]>(GET_ALL_LISTINGS_URL);
  }

  create_new_listing(new_listing: Product): Observable<Product> {
    return this.http.post<Product>(
      CREATE_NEW_LISTING_URL,
      this.product_to_JSON(new_listing),
      HTTP_OPTIONS
    );
  }

  edit_listing(edited_listing: Product): Observable<Product> {
    let listing_id: string = edited_listing.product_id.toString();
    return this.http.put<Product>(
      EDIT_LISTING_DETAIL_URL + listing_id,
      this.product_to_JSON(edited_listing),
      HTTP_OPTIONS
    );
  }

  delete_listing(listing_id: string): Observable<void> {
    return this.http.delete<void>(DELETE_LISTING_URL + listing_id);
  }
}
