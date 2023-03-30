import { Car } from "./Car";
import { CarWorkshop } from "./CarWorkshop";

export interface CarTunedBy{
    id:number;
    CarID:Car;
    CarWorkshopID:CarWorkshop;
    DateTuned:string;
    TuningPrice:number;
    
}