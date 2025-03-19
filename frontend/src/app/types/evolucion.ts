export interface Evolucion {
    id: {
        fechaYHora: string; // Consider using Date if needed
    };
    temperatura: number;
    glucosa: number;
    leucocitos: number;
    hemoglobina: number;
    plaquetas: number;
    colesterol: number;
    hdl: number;
    ldl: number;
    trigliceridos: number;
    sodio: number;
    potasio: number;
    cloro: number;
    creatinina: number;
    urea: number;
    ast: number;
    alt: number;
    bilirrubina: number;
    ph: number;
    pco2: number;
    po2: number;
    hco3: number;
    lactato: number;
    frecuenciarespiratoria: number;
    frecuenciaCardiaca: number;
    saturacionoxigeno: number;
    presionSistolica: number;
    presionDiastolica: number;
}
