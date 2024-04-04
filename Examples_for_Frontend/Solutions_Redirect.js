import React, { useState, useEffect } from 'react';
import { Redirect } from 'react-router-dom';

function CheckImbalanceButton() {
    const [redirect, setRedirect] = useState(false);
    const [imbalancedChakras, setImbalancedChakras] = useState([]);

    const checkImbalance = async () => {
        // Fetch the data from your Flask backend
        const response = await fetch('/path_to_your_flask_endpoint');
        const data = await response.json();

        // Set the imbalanced chakras
        setImbalancedChakras(data.imbalancedChakras);

        // Redirect the user to the solutions page
        setRedirect(true);
    };

    if (redirect) {
        return <Redirect to={{
            pathname: '/solutions',
            state: { imbalancedChakras: imbalancedChakras }
        }} />
    }

    return <button onClick={checkImbalance}>Check Imbalance</button>;
}

function SolutionsPage(props) {
    const imbalancedChakras = props.location.state.imbalancedChakras;

    return (
        <div>
            <h1>Solutions for Imbalanced Chakras</h1>
            <p>The following chakras are imbalanced: {imbalancedChakras.join(', ')}</p>
            {/* Display the solutions for the imbalanced chakras here */}
        </div>
    );
}
