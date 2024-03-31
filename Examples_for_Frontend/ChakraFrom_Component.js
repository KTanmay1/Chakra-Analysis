import React, { useState } from 'react';
import axios from 'axios';

const ChakraForm = () => {
    const [answers, setAnswers] = useState(Array(25).fill('no'));

    const handleChange = (index, value) => {
        setAnswers(prevAnswers => {
            const newAnswers = [...prevAnswers];
            newAnswers[index] = value;
            return newAnswers;
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const data = {
            root: answers.slice(0, 5),
            sacral: answers.slice(5, 10),
            solarPlexus: answers.slice(10, 15),
            heart: answers.slice(15, 20),
            throat: answers.slice(20, 25)
        };

        try {
            const response = await axios.post('http://localhost:5000/store_answers', data);
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {answers.map((answer, index) => (
                <div key={index}>
                    <label>
                        Question {index + 1}
                        <select value={answer} onChange={event => handleChange(index, event.target.value)}>
                            <option value="no">No</option>
                            <option value="yes">Yes</option>
                        </select>
                    </label>
                </div>
            ))}
            <button type="submit">Submit</button>
        </form>
    );
};

export default ChakraForm;
