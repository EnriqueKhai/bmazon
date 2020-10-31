import { Component, OnInit } from '@angular/core';
import { Product } from '../interfaces';
import { ProductService } from '../services/product/product.service';

@Component({
  selector: 'app-listings-page',
  templateUrl: './listings-page.component.html',
  styleUrls: ['./listings-page.component.css']
})
export class ListingsPageComponent implements OnInit {
  listings: Product[];

  constructor(
    private productService: ProductService
  ) { }

  ngOnInit(): void {
    this.productService.getProducts()
        .subscribe(products => this.listings = products);
  }

}
