import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Product } from '../interfaces';
import { ProductService } from '../services/product/product.service';

@Component({
  selector: 'app-create-listing-page',
  templateUrl: './create-listing-page.component.html',
  styleUrls: ['./create-listing-page.component.css']
})
export class CreateListingPageComponent implements OnInit {
  constructor(
    private router: Router,
    private product_service: ProductService,
  ) { }

  ngOnInit(): void {
  }

  onSubmit(new_listing: Product): void {
    this.product_service.create_new_listing(new_listing)
      .subscribe(() => this.router.navigateByUrl("/listings"));
  }
}
