import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateListingPageComponent } from './create-listing-page/create-listing-page.component';
import { EditListingPageComponent } from './edit-listing-page/edit-listing-page.component';
import { ListingDetailPageComponent } from './listing-detail-page/listing-detail-page.component';
import { ListingsPageComponent } from './listings-page/listings-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { MyListingsPageComponent } from './my-listings-page/my-listings-page.component';
import { SignupPageComponent } from './signup-page/signup-page.component';

const routes: Routes = [
  { path: '', redirectTo: '/listings', pathMatch: 'full' },
  { path: 'create-listing', component: CreateListingPageComponent},
  { path: 'edit-listing/:listing_id', component: EditListingPageComponent },
  { path: 'listings/:listing_id', component: ListingDetailPageComponent },
  { path: 'listings', component: ListingsPageComponent },
  { path: 'my-listings', component: MyListingsPageComponent },
  { path: 'signup', component: SignupPageComponent },
  { path: 'login', component: LoginPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
