import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { UserRegistrationForm } from 'src/app/interfaces';

// HTTP configurations.
const HTTP_OPTIONS = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
  })
};

// Authentication URLS.
const USER_SIGNUP_URL: string = "http://localhost:8000/auth/sign_up";
const USER_LOGIN_URL: string = "http://localhost:8000/auth/login";

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(
    private http: HttpClient
  ) { }

  registerNewUser(signup_credentials: UserRegistrationForm): Observable<any> {
    return this.http.post<any>(
      USER_SIGNUP_URL,
      signup_credentials,
      HTTP_OPTIONS
    );
  }

  loginExistingUser(login_credentials): Observable<any> {
    return this.http.post<any>(
      USER_LOGIN_URL,
      login_credentials,
      HTTP_OPTIONS
    );
  }
}
