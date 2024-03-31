import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ImbalancedChakras = () => {
    const [chakras, setChakras] = useState([]);

    useEffect(() => {
        const fetchChakras = async () => {
            try {
                const response = await axios.get('http://localhost:5000/get_imbalanced_chakras');
                setChakras(response.data.chakras);
            } catch (error) {
                console.error(error);
            }
        };

        fetchChakras();
    }, []);

    return (
        <div>
            <h1>Imbalanced Chakras</h1>
            {chakras.length > 0 ? (
                <ul>
                    {chakras.map((chakra, index) => (
                        <li key={index}>{chakra}</li>
                    ))}
                </ul>
            ) : (
                <p>No imbalanced chakras</p>
            )}
        </div>
    );
};

export default ImbalancedChakras;
