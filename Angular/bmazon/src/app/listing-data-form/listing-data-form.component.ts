import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { Product } from '../interfaces';

@Component({
  selector: 'app-listing-data-form',
  templateUrl: './listing-data-form.component.html',
  styleUrls: ['./listing-data-form.component.css']
})
export class ListingDataFormComponent implements OnInit {
  @Input() listing = {} as Product;
  @Input() button_text: string = "Submit";
  @Output() on_submit = new EventEmitter<Product>();

  constructor(
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.on_submit.emit(this.listing);
  }
}
