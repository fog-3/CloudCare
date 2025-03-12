import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderPatientsComponent } from './header-patients.component';

describe('HeaderPatientsComponent', () => {
  let component: HeaderPatientsComponent;
  let fixture: ComponentFixture<HeaderPatientsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderPatientsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderPatientsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
