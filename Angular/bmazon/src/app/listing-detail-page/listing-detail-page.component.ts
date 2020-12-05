import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Product } from '../interfaces';
import { ProductService } from '../services/product/product.service';

@Component({
  selector: 'app-listing-detail-page',
  templateUrl: './listing-detail-page.component.html',
  styleUrls: ['./listing-detail-page.component.css']
})
export class ListingDetailPageComponent implements OnInit {
  listing = {} as Product;

  constructor(
    private route: ActivatedRoute,
    private product_service: ProductService,
  ) { }

  ngOnInit(): void {
    let listing_id = this.route.snapshot.paramMap.get('listing_id');
    this.product_service.get_listing_by_ID(listing_id)
        .subscribe(listing => this.listing = listing["results"][0]);
  }
}
