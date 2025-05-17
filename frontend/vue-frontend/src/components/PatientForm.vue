<template>
    <div id="formAddPatient">
        <form @submit.prevent="addPatient">
            <label for="firstName">First Name</label>
            <input v-model="form.firstName" placeholder="Will" required />
            <label for="LastName">Last Name</label>
            <input v-model="form.lastName" placeholder="Smith" required />
            <label for="age">Age</label>
            <input v-model.number="form.age" type="number" placeholder="25" required />
            <label for="email">E-mail</label>
            <input v-model="form.email" type="email" placeholder="example@example.com" required />
            <label for="phone">Phone</label>
            <input v-model="form.phone" placeholder="+33 78965424" required />
            <button type="submit">Validate</button>
        </form>
    </div>
</template>

<style scoped>
    form {
        display: flex;
        flex-direction: column;
        gap: 12px;
        width: 500px;
        margin-top: 20px;
        background: #f9f9f9;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    label {
        font-weight: bold;
        margin-bottom: 4px;
    }

    input {
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        margin-top: 10px;
    }
</style>


<script setup>
import { ref, onMounted } from 'vue';
import { getPatients, postPatient } from '../services/api.js';

const emit = defineEmits(['submitted'])

// Patients list
const patients = ref([]);

const form = ref({
    firstName: '',
    lastName: '',
    age: null,
    email: '',
    phone: ''
});

const loadPatients = async () => {
    patients.value = await getPatients();
};

onMounted(() => {
    loadPatients();
});

const addPatient = async () => {
    const response = await postPatient(form.value);
    if (response) {
        await loadPatients();
        form.value = { firstName: '', lastName: '', age: null, email: '', phone: '' };

        emit('submitted');
    }
};
</script>
