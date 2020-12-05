import { Component, OnInit } from '@angular/core';
import { Product } from '../interfaces';
import { ProductService } from '../services/product/product.service';

@Component({
  selector: 'app-listings-page',
  templateUrl: './listings-page.component.html',
  styleUrls: ['./listings-page.component.css']
})
export class ListingsPageComponent implements OnInit {
  all_listings = [] as Product[];

  constructor(
    private product_service: ProductService
  ) { }

  ngOnInit(): void {
    this.product_service.get_all_listings()
        .subscribe(all_listings => this.all_listings = all_listings["results"]);
  }
}
