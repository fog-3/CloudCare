import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EvolutionPatientComponent } from './evolution-patient.component';

describe('EvolutionPatientComponent', () => {
  let component: EvolutionPatientComponent;
  let fixture: ComponentFixture<EvolutionPatientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EvolutionPatientComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EvolutionPatientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
