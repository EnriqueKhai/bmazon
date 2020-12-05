import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from '../interfaces';
import { ProductService } from '../services/product/product.service';

@Component({
  selector: 'app-edit-listing-page',
  templateUrl: './edit-listing-page.component.html',
  styleUrls: ['./edit-listing-page.component.css']
})
export class EditListingPageComponent implements OnInit {
  listing = {} as Product;

  // Render the form only after the listing has been loaded.
  listing_is_loaded: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private product_service: ProductService,
  ) { }

  ngOnInit(): void {
    let listing_id = this.route.snapshot.paramMap.get('listing_id');
    this.product_service.get_listing_by_ID(listing_id)
        .subscribe(product => {
          this.listing = product["results"][0];
          this.listing_is_loaded = true;
        })
  }

  onSubmit(edited_listing: Product): void {
    this.product_service.edit_listing(edited_listing)
      .subscribe(() => this.router.navigateByUrl("/listings"));
  }
}
