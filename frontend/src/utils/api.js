import config from "../frontendconfig/frontend_config";

/**
 * Fetch data from the API.
 * @param {string} endpoint - The API endpoint to fetch data from.
 * @param {object} options - Fetch options (method, headers, body, etc.).
 * @returns {Promise<object>} - The response data as JSON.
 */
export async function fetchData(endpoint, options = {}) {
    const response = await fetch(`${config.BACKEND_URL}/${endpoint}`, options);
    if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
    }
    return response.json();
}

/**
 * Example function to get user data.
 * @param {string} userId - The ID of the user to fetch.
 * @returns {Promise<object>} - The user data.
 */
export async function getUser(userId) {
    return fetchData(`users/${userId}`);
}

/**
 * Example function to create a new portfolio.
 * @param {object} portfolioData - The data for the new portfolio.
 * @returns {Promise<object>} - The created portfolio data.
 */
export async function createPortfolio(portfolioData) {
    return fetchData(`portfolios`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(portfolioData),
    });
}
