import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../../interfaces';


@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private products_url: string = "http://localhost:8000/api/products/";

  constructor(
    private http: HttpClient
  ) { }

  getProduct(listing_id: string): Observable<Product> {
    return this.http.get<Product>(this.products_url + listing_id);
  }

  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.products_url);
  }
}
