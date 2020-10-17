import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateListingPageComponent } from './create-listing-page.component';

describe('CreateListingPageComponent', () => {
  let component: CreateListingPageComponent;
  let fixture: ComponentFixture<CreateListingPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateListingPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateListingPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
