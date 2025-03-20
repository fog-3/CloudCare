import { Paciente } from "./pacientes";

export interface MessageE {
    session_id: string;
    question: string;
    paciente: Paciente;
    esGrafico: boolean;
    esResumenEvolutivo: boolean;
}