export interface Paciente {
    nombre: string;
    edad: number;
    sexo: "M" | "F";
    alergias: string | null;
    motivoingreso: string;
    diagnosticoprincipal: string;
    condicionesprevias: string;
    fechaingreso: string;
    servicio: string;
    estadoalingreso: string;
    pacienteid: number;
}
