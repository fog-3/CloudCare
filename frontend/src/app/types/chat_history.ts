export interface ChatHistory {
    session_id:  string ;
    role: "user" | "assistant";
    message: string;
    timestamp: string;
}