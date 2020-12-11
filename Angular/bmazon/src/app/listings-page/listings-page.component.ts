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

  delete_listing(listing_id_int: number): void {
    // Remove listing from UI.
    let listing_index = this.all_listings.findIndex(listing => listing.product_id === listing_id_int);
    this.all_listings.splice(listing_index,1);

    // Make the HTTP DELETE request.
    let listing_id_str = listing_id_int.toString();
    this.product_service.delete_listing(listing_id_str)
      .subscribe(() => {});
  }
}
