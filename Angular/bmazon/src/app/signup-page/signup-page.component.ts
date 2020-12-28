import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../services/authentication/authentication.service';
import { UserRegistrationForm } from 'src/app/interfaces';

@Component({
  selector: 'app-signup-page',
  templateUrl: './signup-page.component.html',
  styleUrls: ['./signup-page.component.css']
})
export class SignupPageComponent implements OnInit {
  signup_credentials: UserRegistrationForm = {
    email: "",
    first_name: "",
    last_name: "",
    address: "",
    country: "",
    city: "",
    postal_code: null,
    account_type: "",
    user: {
      username: "",
      password: ""
    },
    password2: "",
  };

  constructor(
    private auth: AuthenticationService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  register(): void {
    this.auth.registerNewUser(this.signup_credentials)
      .subscribe(
        response => {
          if ("response" in response) {
            if (response.response === "successfully registered a new user") {
              alert("Successfully registered new user!");
              this.router.navigateByUrl("/listings");
            } else {
              alert("Error occurred in registering new user.");
            }
          } else {
            alert("Error occurred in registering new user.");
          }
        },
        error => {
          console.log(error);
        }
      );
  }
}
