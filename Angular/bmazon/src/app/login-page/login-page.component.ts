import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../services/authentication/authentication.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {
  login_credentials = {
    username: "",
    password: ""
  };

  constructor(
    private auth: AuthenticationService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  login(): void {
    this.auth.loginExistingUser(this.login_credentials)
      .subscribe(
        response => {
          if ("token" in response) {
            alert("Logged in successfully!");
            this.router.navigateByUrl("/listings");
          } else {
            console.log(response);
            alert("Log in unsuccessful.");
          }
        },
        error => {
          console.log(error);
          alert("Error occurred while logging in.");
        }
      );
  }
}
