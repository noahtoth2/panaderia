const API_URL = "http://localhost:8000"; // Cambia si tu backend usa otro puerto

export async function login(username, password) {
    const res = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Error desconocido");
    }

    return await res.json(); // { access_token: "...", token_type: "bearer" }
}
